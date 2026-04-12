"""
General Account - Central persistent funding source for all silos.
Simple cash ledger with 25% per-silo allocation rule (mutable for future).
Saves/loads state from data/general_account.json so balance survives restarts.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

class GeneralAccount:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.file_path = self.data_dir / "general_account.json"
        
        self.balance: float = 100.0
        self.funding_history: list = []
        self.last_funding_date = datetime.now()
        
        self._load_state()  # Load persisted data if exists

    def _load_state(self):
        """Load General Account state from JSON if file exists."""
        if self.file_path.exists():
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                
                self.balance = data.get("balance", 100.0)
                self.funding_history = data.get("funding_history", [])
                last_date_str = data.get("last_funding_date")
                if last_date_str:
                    self.last_funding_date = datetime.fromisoformat(last_date_str)
                
                print(f"✅ General Account loaded from disk. Balance: ${self.balance:.2f}")
            except Exception as e:
                print(f"⚠️  Could not load General Account state: {e}. Starting fresh.")
        else:
            print(f"🆕 First run detected. General Account initialized with ${self.balance:.2f}")
            self._save_state()

    def _save_state(self):
        """Save current state to JSON file."""
        try:
            data = {
                "balance": round(self.balance, 2),
                "funding_history": self.funding_history,
                "last_funding_date": self.last_funding_date.isoformat(),
                "last_updated": datetime.now().isoformat()
            }
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"⚠️  Could not save General Account state: {e}")

    def get_available_funding(self, silo_name: str) -> float:
        """25% of current General Account balance per silo (easy to change later)."""
        max_per_silo = self.balance * 0.25
        return max(0.0, round(max_per_silo, 2))

    def allocate_to_silo(self, silo_name: str, requested_amount: float) -> float:
        """Allocate funds with 25% cap. Returns actual amount given."""
        available = self.get_available_funding(silo_name)
        actual_amount = min(requested_amount, available)
        
        if actual_amount > 0:
            self.balance -= actual_amount
            self.funding_history.append({
                "timestamp": datetime.now().isoformat(),
                "silo": silo_name,
                "amount": round(actual_amount, 2),
                "remaining_balance": round(self.balance, 2)
            })
            self.last_funding_date = datetime.now()
            self._save_state()
            
            print(f"✅ General Account → Allocated ${actual_amount:.2f} to {silo_name} "
                  f"(Remaining General: ${self.balance:.2f})")
            return actual_amount
        else:
            print(f"⚠️  General Account: No funds available or limit reached for {silo_name}")
            return 0.0

    def receive_from_silo(self, silo_name: str, amount: float):
        """Receive profits or returned capital from a silo."""
        if amount > 0:
            self.balance += amount
            self.funding_history.append({
                "timestamp": datetime.now().isoformat(),
                "silo": silo_name,
                "amount": round(-amount, 2),   # negative = inflow to General
                "remaining_balance": round(self.balance, 2)
            })
            self.last_funding_date = datetime.now()
            self._save_state()
            
            print(f"📥 General Account ← Received ${amount:.2f} from {silo_name} "
                  f"(New General Balance: ${self.balance:.2f})")

    def get_status(self) -> dict:
        """Return current status."""
        return {
            "general_balance": round(self.balance, 2),
            "total_fundings": len(self.funding_history),
            "last_funding_date": self.last_funding_date.strftime("%Y-%m-%d %H:%M")
        }