#!/usr/bin/env python3
"""
Flux Kontext Max — Context-aware maximum quality image generation
Advanced Options Example — Explore all available parameters

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/flux-kontext-max/pricing

Model: flux-kontext-max
"""

from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

print("🔧 flux-kontext-max — Advanced Options Demo")
print("=" * 60)

# ── Size Variations ───────────────────────────────────────────────────────────
print("\n📐 Testing different sizes...")
sizes = [
    (512, 512, "Square (512x512)"),
    (1024, 1024, "Square HD (1024x1024)"),
    (1024, 768, "Landscape (1024x768)"),
    (768, 1024, "Portrait (768x1024)"),
]

for width, height, label in sizes:
    result = client.images.generate(
        model="flux-kontext-max",
        prompt="a beautiful sunset over mountains, photorealistic, 8k",
        width=width,
        height=height,
    )
    print(f"  ✅ {label}: {result.url}")

# ── Style Variations ───────────────────────────────────────────────────────────
print("\n🎨 Testing different styles...")
style_prompts = [
    ("a beautiful sunset over mountains, photorealistic, 8k, photorealistic, DSLR quality", "Photorealistic"),
    ("a beautiful sunset over mountains, photorealistic, 8k, oil painting, impressionist style", "Oil Painting"),
    ("a beautiful sunset over mountains, photorealistic, 8k, anime style, vibrant colors", "Anime"),
    ("a beautiful sunset over mountains, photorealistic, 8k, pencil sketch, detailed linework", "Sketch"),
]

for prompt, style_name in style_prompts:
    result = client.images.generate(
        model="flux-kontext-max",
        prompt=prompt,
        width=1024,
        height=1024,
    )
    print(f"  ✅ {style_name}: {result.url}")

# ── Negative Prompt (if supported) ────────────────────────────────────────────
print("\n🚫 Using negative prompts...")
try:
    result = client.images.generate(
        model="flux-kontext-max",
        prompt="a beautiful sunset over mountains, photorealistic, 8k",
        negative_prompt="blurry, low quality, distorted, ugly",
        width=1024,
        height=1024,
    )
    print(f"  ✅ With negative prompt: {result.url}")
except Exception as e:
    print(f"  ℹ️  Negative prompt not supported: {e}")

print("\n✅ Advanced options demo complete!")
print("📖 Full API docs: https://nexa-api.com/docs")
print("💰 Pricing: https://rapidapi.com/nexaquency/flux-kontext-max/pricing")
