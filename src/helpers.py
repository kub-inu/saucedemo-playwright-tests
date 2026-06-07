def summary_price(product_test_data: dict, tax_rate: float) -> dict:
    """
    Pomocná funkce pro výpočet celkové ceny produktů bez daně, výše daně a celkové ceny s daní.

    Args:
        product_test_data: Slovník s testovacími daty produktů.
        tax_rate: Sazba daně. Výchozí hodnota je 0.08, tedy 8 %.

    Returns:
        Slovník s cenou bez daně, daní a cenou s daní.
    """
    total_price = 0.0

    for item in product_test_data.values():
        total_price += float(item["price"])

    tax = total_price * tax_rate
    total_price_with_tax = total_price + tax

    return {
        "summary_price_without_tax": round(total_price, 2),
        "tax": round(tax, 2),
        "summary_price_with_tax": round(total_price_with_tax, 2)
    }