#!/usr/bin/env python3
"""
Flux Kontext Max — Context-aware maximum quality image generation

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/flux-kontext-max/pricing

Model: flux-kontext-max
"""

from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
# Replace with your actual API key from https://nexa-api.com
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

# ── Basic Usage ────────────────────────────────────────────────────────────────
print("Starting flux-kontext-max generation...")

result = client.images.generate(
    model="flux-kontext-max",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
)

print(f"✅ Generation complete!")
print(f"   Image url: {result.url}")
print(f"   Job ID: {result.job_id}")
print(f"   Status: {result.status}")
