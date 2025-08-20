# AUDIO BPM ADJUST
----
使用**librosa**与**pyrubberband**对文件夹中的音频文件进行bpm分析并进行加速/减速使得结果符合指定的bpm。

能够将喜欢的歌曲处理为180bpm或目标bpm的音乐当作跑步歌单

*注意 
因为使用librosa拉伸音频的效果较差，因此使用了pyrubberband作为音频处理工具，在Windows中可能要下载rubberband的执行程序并添加到path中