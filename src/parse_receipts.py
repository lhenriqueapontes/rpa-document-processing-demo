from pathlib import Path
import argparse
import re
import pandas as pd

PATTERNS = {
    'store': r'Store: (.+)',
    'date': r'Date: (.+)',
    'item': r'Item: (.+)',
    'quantity': r'Quantity: (\d+)',
    'unit_price': r'Unit price: ([0-9.]+)',
    'total': r'Total: ([0-9.]+)',
    'payment': r'Payment: (.+)',
}


def parse_text(text):
    record = {}
    for key, pattern in PATTERNS.items():
        match = re.search(pattern, text)
        record[key] = match.group(1).strip() if match else None
    return record


def parse_folder(input_dir='data/receipts_txt', output='reports/parsed_receipts.csv'):
    rows = []
    for path in sorted(Path(input_dir).glob('*.txt')):
        record = parse_text(path.read_text(encoding='utf-8'))
        record['source_file'] = path.name
        rows.append(record)
    df = pd.DataFrame(rows)
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', default='data/receipts_txt')
    parser.add_argument('--output', default='reports/parsed_receipts.csv')
    args = parser.parse_args()
    print(parse_folder(args.input_dir, args.output))


if __name__ == '__main__':
    main()
