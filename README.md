# GPU Chatbot Colab

A powerful chatbot powered by the Qwen2.5-3B-Instruct model, optimized to run on Google Colab with GPU acceleration.

## Features

- 🚀 **GPU Accelerated**: Runs efficiently on NVIDIA T4 GPUs in Google Colab
- 🤖 **Advanced Model**: Uses Qwen/Qwen2.5-3B-Instruct for high-quality responses
- 💬 **Conversation History**: Maintains context across multiple turns for coherent interactions
- ⚡ **Fast Inference**: Optimized for quick response generation
- 📊 **Model Monitoring**: Displays GPU and memory information

## Requirements

- Google Colab with T4 GPU enabled
- Python 3.7+
- CUDA-compatible GPU (T4 recommended)

## Installation & Setup

1. Open the notebook in Google Colab
2. Go to **Runtime → Change runtime type → Select GPU (T4)**
3. Run the cells in order:
   - First cell: Verify GPU availability
   - Second cell: Download and load the Qwen2.5-3B-Instruct model
   - Third cell: Initialize the chatbot

## Usage

The chatbot supports multi-turn conversations with maintained history. Users can interact by providing text input, and the model will generate contextual responses.

### Example

```python
response = chat("What is machine learning?", max_new_tokens=512)
print(response)
```

## Model Details

- **Model Name**: Qwen/Qwen2.5-3B-Instruct
- **Size**: ~2GB
- **Precision**: float16 (for optimal memory usage)
- **Device**: CUDA (GPU) or CPU fallback

## Performance

- Recommended GPU: NVIDIA T4 (available in Colab)
- Memory Usage: ~3-4GB VRAM
- Inference Speed: Fast on T4 GPU

## Features Included

- Automatic GPU detection and optimization
- Model weight downloading and caching
- Conversation history management
- System prompt configuration
- Configurable generation parameters

## Troubleshooting

**No GPU Available?**
- Go to Runtime → Change runtime type
- Select "GPU" and choose T4
- Reconnect to the runtime

**Out of Memory?**
- Reduce `max_new_tokens` parameter
- Clear conversation history periodically
- Use CPU if GPU VRAM is exhausted

## License

MIT License

## Author

Created for efficient GPU-accelerated chatbot inference on Google Colab.
