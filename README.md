# Flux Kontext Max API — Python SDK

> Maximum quality context-aware image generation.

[![PyPI](https://img.shields.io/pypi/v/nexa-ai)](https://pypi.org/project/nexa-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Flux Kontext Max** via NexaAPI — the cheapest and fastest Image Generation API. Starting at **$0.08/image**.

🔗 **[Get API Key on RapidAPI](https://rapidapi.com/nexaquency/flux-kontext-max/pricing)**

## 🚀 Quick Start

```bash
pip install nexa-ai
```

```python
from nexa_ai import NexaAI

client = NexaAI(api_key="your-api-key")  # Get key at https://nexa-api.com

result = client.images.generate(
    model="flux-kontext-max",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
)
print(result.url)  # Direct URL to generated image
```

## ⚡ NEW: One-Step API (No Polling!)

```python
import requests

response = requests.post(
    'https://nexa-api.com/v1/generate',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},
    json={'model': 'flux-2-pro', 'prompt': 'a sunset over mountains', 'image_size': 'landscape_4_3'}
)
image_url = response.json()['result']['outputs'][0]['url']
print(image_url)  # https://nexa-api.com/v1/files/...
```

**One request → direct result. No polling needed.**

## 💰 Pricing

| Model | Price | Speed |
|-------|-------|-------|
| **Flux Kontext Max** | **$0.08/image** | Fast |

Compare with competitors:
- **Replicate**: 2-5x more expensive
- **FAL.ai**: Similar pricing, fewer models
- **Together AI**: Limited image models

👉 **[Full pricing comparison](https://nexa-api.com/pricing)**

## 📦 Installation

```bash
# pip
pip install nexa-ai

# poetry
poetry add nexa-ai

# conda
pip install nexa-ai
```

## 🔧 Usage Examples

### Basic Image Generation

```python
from nexa_ai import NexaAI

client = NexaAI(api_key="your-api-key")

result = client.images.generate(
    model="flux-kontext-max",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
)
print(result.url)
print(result.job_id)
print(result.status)
```

### Async Usage

```python
import asyncio
from nexa_ai import AsyncNexaAI

async def main():
    client = AsyncNexaAI(api_key="your-api-key")
    result = await client.images.generate(
    model="flux-kontext-max",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
    )
    print(result.url)

asyncio.run(main())
```

### Using with RapidAPI

```python
from nexa_ai import NexaAI

# Use your RapidAPI key instead
client = NexaAI(
    api_key="your-rapidapi-key",
    base_url="https://flux-kontext-max.p.rapidapi.com" if model.get('rapidapi_slug') else "https://nexa-api.com",
)
```

## 🤖 Available Models

NexaAPI offers **56+ AI models** across image, video, and audio generation:

### Image Generation
Flux Schnell, Flux Dev, Flux Pro, Flux 2 Pro, Flux 2 Max, GPT-Image 1.5, Gemini 3 Pro, Stable Diffusion 3.5, SDXL, Ideogram v2, Recraft v3, and more.

### Video Generation
Kling v3 Pro, Veo 3.1, Sora 2, Minimax Video, Hunyuan Video, and more.

### Audio
ElevenLabs v3, OpenAI TTS, Kokoro TTS, Suno v4.5, Udio v2, and more.

👉 **[See all models](https://nexa-api.com/models)**

## 🔗 Links

- **Website**: [nexa-api.com](https://nexa-api.com)
- **API Docs**: [nexa-api.com/docs](https://nexa-api.com/docs)
- **Pricing**: [nexa-api.com/pricing](https://nexa-api.com/pricing)
- **RapidAPI**: [rapidapi.com/nexaquency](https://rapidapi.com/nexaquency)
- **PyPI**: [pypi.org/project/nexa-ai](https://pypi.org/project/nexa-ai/)
- **npm**: [npmjs.com/package/nexa-ai](https://www.npmjs.com/package/nexa-ai)

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Keywords**: Flux Kontext Max API, Flux Kontext Max Python, Flux Kontext Max API pricing, cheapest Flux Kontext Max API, Image Generation API, AI API, NexaAPI, text to image API, AI image generation
