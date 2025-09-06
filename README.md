
# Summary
- python: 生成mid文件
- timidity: 生成wav文件
- afplay: 可以在mac上播放wav

# Preparation
```
brew install timidity
```

# Example
```
# Create mid
$ source venv/bin/activate
$ python3 komoriuta_piano.py
$ deactivate

# Transform mid to wav
$ timidity komoriuta_piano.mid -Ow -o komoriuta_piano.wav

# Play
$ afplay komoriuta_piano.wav
```
