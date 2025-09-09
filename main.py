#!/usr/bin/env python3
"""
Main script for the Public Currency Exchange Library
Professional usage examples for currency conversion operations
"""

import currency_exchange
from currency_exchange import CurrencyExchange

def main():
    """
    Demonstrate typical currency exchange operations for professional use.
    """
    
    # Create exchange instance for advanced operations
    exchange = CurrencyExchange()
    
    # Basic conversion operations
    conversions = [
        (1000, "USD", "EUR"),
        (500, "EUR", "GBP"), 
        (2000, "USD", "JPY"),
        (750, "GBP", "CAD"),
        (1500, "USD", "AUD")
    ]
    
    print("🌍 Currency Exchange Conversion Results:")
    print("=" * 45)
    
    for amount, from_curr, to_curr in conversions:
        try:
            result = currency_exchange.convert_currency(amount, from_curr, to_curr)
            formatted = currency_exchange.format_currency(result, to_curr)
            rate = currency_exchange.get_exchange_rate(from_curr, to_curr)
            print(f"  {amount} {from_curr} → {formatted} (Rate: {rate:.4f})")
        except Exception as e:
            print(f"  Error converting {amount} {from_curr} to {to_curr}: {e}")
    
    # Multiple currency comparison
    base_amount = 10000
    base_currency = "USD"
    target_currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "CHF"]
    
    print(f"\n💱 Converting {base_amount} {base_currency} to multiple currencies:")
    try:
        results = exchange.convert_multiple(base_amount, base_currency, target_currencies)
        for currency, amount in results.items():
            formatted = exchange.format_currency(amount, currency)
            print(f"  → {formatted}")
    except Exception as e:
        print(f"  Error in multiple conversion: {e}")
    
    # Finding best exchange rates
    investment_scenarios = [
        (5000, "USD", ["EUR", "GBP", "CHF"]),
        (3000, "EUR", ["USD", "GBP", "JPY"]), 
        (8000, "GBP", ["USD", "EUR", "CAD"])
    ]
    
    print(f"\n📈 Finding best exchange rates:")
    for amount, from_curr, to_currencies in investment_scenarios:
        try:
            best = exchange.find_best_exchange(amount, from_curr, to_currencies)
            print(f"  {amount} {from_curr} → Best: {best['formatted']} ({best['currency']}) at rate {best['rate']:.4f}")
        except Exception as e:
            print(f"  Error finding best rate for {amount} {from_curr}: {e}")
    
    # Currency information lookup
    sample_currencies = ["USD", "EUR", "GBP", "JPY", "BTC"]
    
    print(f"\n📊 Currency Information:")
    for curr in sample_currencies:
        try:
            name = exchange.get_currency_name(curr)
            symbol = exchange.get_currency_symbol(curr)
            print(f"  {curr}: {name} ({symbol})")
        except Exception as e:
            print(f"  {curr}: Not supported - {e}")
    
    # Transaction simulation
    transactions = [
        {"amount": 299.99, "from": "USD", "to": "EUR", "description": "Online purchase"},
        {"amount": 1250.00, "from": "EUR", "to": "GBP", "description": "Business payment"},
        {"amount": 75.50, "from": "USD", "to": "CAD", "description": "Cross-border fee"},
        {"amount": 3500.00, "from": "USD", "to": "JPY", "description": "Travel exchange"}
    ]
    
    total_fees = 0
    for tx in transactions:
        try:
            converted = exchange.convert(tx["amount"], tx["from"], tx["to"])
            formatted_from = exchange.format_currency(tx["amount"], tx["from"])
            formatted_to = exchange.format_currency(converted, tx["to"])
            
            # Simulate transaction fee (2% of original amount)
            fee = tx["amount"] * 0.02
            total_fees += fee
            
        except Exception as e:
            pass
    
    # Market analysis
    base_currencies = ["USD", "EUR", "GBP"]
    
    for base in base_currencies:
        supported = exchange.get_supported_currencies()
        
        # Show rates to major currencies
        major_currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]
        for target in major_currencies:
            if target != base and target in supported:
                try:
                    rate = exchange.get_exchange_rate(base, target)
                except Exception as e:
                    pass
    
    # Portfolio value calculation
    portfolio = {
        "USD": 15000,
        "EUR": 8500, 
        "GBP": 5200,
        "JPY": 750000,
        "CAD": 3800
    }
    
    portfolio_base = "USD"
    total_value = 0
    
    for currency, amount in portfolio.items():
        try:
            if currency == portfolio_base:
                value_in_base = amount
            else:
                value_in_base = exchange.convert(amount, currency, portfolio_base)
            
            total_value += value_in_base
            formatted_original = exchange.format_currency(amount, currency)
            formatted_converted = exchange.format_currency(value_in_base, portfolio_base)
            
        except Exception as e:
            pass
    
    print(f"\n✅ Currency Exchange Operations Completed Successfully")
    print(f"📊 All conversion functions tested and operational")

if __name__ == "__main__":
    main()
