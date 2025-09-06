from midiutil import MIDIFile

# 创建MIDI对象
mf = MIDIFile(1)  
track = 0
time = 0
mf.addTrackName(track, time, "Komoriuta")
mf.addTempo(track, time, 80)

channel = 0
volume = 100

# 右手旋律 (C4=60)
right_notes = [67, 69, 70, 65, 67, 69, 71, 72, 74, 71, 72, 74, 75, 72, 74, 71]

# 左手和弦
left_chords = [
    [43, 46, 52], [41, 45, 50],
    [43, 47, 50], [48, 52, 55],
    [41, 45, 48], [43, 47, 50],
    [48, 52, 55], [50, 54, 57]
]

# 添加右手旋律 (每个四分音符)
time = 0
for n in right_notes:
    mf.addNote(track, channel, n, time, 1, volume)
    time += 1

# 添加左手和弦 (每个二分音符)
time = 0
for chord in left_chords:
    for n in chord:
        mf.addNote(track, channel, n, time, 2, volume)
    time += 2

# 保存文件
with open("komoriuta_piano.mid", "wb") as f:
    mf.writeFile(f)

print("✅ 已生成 komoriuta_piano.mid")
