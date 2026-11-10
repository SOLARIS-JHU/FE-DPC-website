"""Render original author PDFs; no curves or scientific data are regenerated.

Dependencies: pypdfium2, Pillow. Run from the repository root.
The optional --svg flag also requires Inkscape on PATH.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    'graphical-abstract': 2600,
    'van-der-pol': 2400,
    'two-tank': 2200,
    'glycolytic-model': 2200,
    'glycolytic-control': 2200,
    'quadrotor': 2400,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--svg', action='store_true')
    args = parser.parse_args()
    target = ROOT / 'assets' / 'figures'
    for name, width in FILES.items():
        pdf = pdfium.PdfDocument(target / (name + '.pdf'))
        page = pdf[0]
        image = page.render(scale=width/page.get_width()).to_pil().convert('RGB')
        image.save(target / (name + '.webp'), quality=95, method=6)
        if name == 'graphical-abstract':
            image.save(target / (name + '.png'))
        print(name, image.size)
        page.close()
        pdf.close()
    if args.svg:
        inkscape = shutil.which('inkscape') or r'C:\Program Files\Inkscape\bin\inkscape.com'
        subprocess.run([inkscape, str(target/'graphical-abstract.pdf'), '--pdf-poppler', '--export-plain-svg', '--export-text-to-path', '--export-filename='+str(target/'graphical-abstract.svg')], check=True)

if __name__ == '__main__':
    main()
