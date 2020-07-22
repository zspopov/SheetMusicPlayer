<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title Page</title>
    <link rel="stylesheet" href="index.css"/>
    
</head>
<body>
    <div class="head">
        <h1>Sheet Music Player</h1>
        <p>by Zhehcko Popov, 62140</p>
        <button class="choose_button" id="twinkle" onclick="play()">Twinkle Twinkle Little Star</button>
        <label for="import" class="input_button">Import</label>
        <input type="file" id="import"></input>
    </div>
    <script src="./index.js"></script>
    <script>
        function play(){
            window.location.href = './SheetMusicPlayer.html';
        }
    </script>
</body>
</html>