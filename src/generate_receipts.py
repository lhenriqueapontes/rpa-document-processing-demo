from pathlib import Path
import argparse
import random

TEMPLATE = '''RECEIPT DEMO
Store: {store}
Date: {date}
Item: {item}
Quantity: {qty}
Unit price: {unit_price:.2f}
Total: {total:.2f}
Payment: {payment}
'''


def generate_receipts(output_dir='data/receipts_txt', n=20, seed=42):
    random.seed(seed)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    stores = ['Alpha Market', 'Beta Office', 'Gamma Services']
    items = ['Paper', 'Keyboard', 'Cloud Plan', 'Notebook', 'Mouse']
    payments = ['card', 'cash', 'invoice']
    for i in range(1, n + 1):
        qty = random.randint(1, 5)
        unit = round(random.uniform(10, 250), 2)
        text = TEMPLATE.format(
            store=random.choice(stores),
            date=f'2025-03-{(i % 28) + 1:02d}',
            item=random.choice(items),
            qty=qty,
            unit_price=unit,
            total=qty * unit,
            payment=random.choice(payments),
        )
        (out / f'receipt_{i:03d}.txt').write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='data/receipts_txt')
    parser.add_argument('--n', type=int, default=20)
    args = parser.parse_args()
    generate_receipts(args.output_dir, args.n)
    print(args.output_dir)


if __name__ == '__main__':
    main()
