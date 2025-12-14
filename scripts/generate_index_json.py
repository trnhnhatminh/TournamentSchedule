#!/usr/bin/env python3
"""Generate index.json files for image folders.

Usage: python3 scripts/generate_index_json.py --root data/image --month Dec
"""
import argparse
import json
import os

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

def generate(root, month):
    month_dir = os.path.join(root, month)
    if not os.path.isdir(month_dir):
        print('Month directory not found:', month_dir)
        return

    for name in sorted(os.listdir(month_dir)):
        day_dir = os.path.join(month_dir, name)
        if not os.path.isdir(day_dir):
            continue
        files = [f for f in sorted(os.listdir(day_dir)) if os.path.splitext(f)[1].lower() in IMAGE_EXTS]
        if not files:
            print('No images in', day_dir)
            continue
        index_path = os.path.join(day_dir, 'index.json')
        with open(index_path, 'w', encoding='utf-8') as fh:
            json.dump(files, fh, ensure_ascii=False)
        print('Wrote', index_path, '(', len(files), 'images)')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='data/image', help='Images root folder')
    p.add_argument('--month', default='Dec', help='Month folder name (e.g., Dec)')
    args = p.parse_args()
    generate(args.root, args.month)
