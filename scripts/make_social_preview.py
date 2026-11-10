"""Compose a social preview from the original method figure (no generated data)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root=Path(__file__).resolve().parents[1]
canvas=Image.new('RGB',(1200,630),'#fbfbfd')
d=ImageDraw.Draw(canvas)
font=lambda n,size: ImageFont.truetype(str(root/'assets/fonts'/n),size)
d.rectangle((0,0,1200,12),fill='#002d72')
d.text((48,38),'SOLARIS  /  L4DC 2026',font=font('font-4.ttf',22),fill='#002d72')
d.text((48,87),'Zero-Shot Function Encoder-Based',font=font('font-1.ttf',43),fill='#1a1f2b')
d.text((48,142),'Differentiable Predictive Control',font=font('font-1.ttf',43),fill='#1a1f2b')
d.text((48,208),'Learn offline. Adapt online through dynamics coefficients.',font=font('font-2.ttf',23),fill='#5b6470')
figure=Image.open(root/'assets/figures/graphical-abstract.png').convert('RGB')
figure.thumbnail((1104,345))
canvas.paste(figure,((1200-figure.width)//2,278))
canvas.save(root/'assets/social-preview.png',optimize=True)
