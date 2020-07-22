import json
import sys

f = open(sys.argv[1]);

data = json.load(f);

min_difference = 10000;
max_difference = 0;
overall_length = 0;
notes_count = 0;

for i in data['track1'] :
    notes_count = notes_count + 1;
    difference = int(i['end']) - int(i['start']);
    if difference < min_difference :
        min_difference = difference;
    if difference > max_difference :
        max_difference = difference;
    overall_length = overall_length + difference;

ratio = max_difference/min_difference;

staves_count = overall_length/min_difference/4;
stave_length = 4*min_difference;
canvasHeightVar = staves_count/2 * 110;

current_length = 0;
index = 0;

def evaluate_difference(difference) :
    if difference == min_difference :
        return "q"
    if difference == min_difference*2 :
        return "h"
    if difference == min_difference*4 :
        return "1/2"

def evaluate_note(note) :
    if note == "c4" :
        return "c/4"
    if note == "d4" :
        return "d/4"
    if note == "e4" :
        return "e/4"
    if note == "f4" :
        return "f/4"
    if note == "g4" :
        return "g/4"
    if note == "a4" :
        return "a/4"
    if note == "b4" :
        return "b/4"

print("var staveCount = " + str(staves_count) + ";");
print("var canvasHeightVar = " + str(canvasHeightVar) + ";");

notes = [];

canvas_x = 10;
canvas_y = 0;
canvas_w = 390;

for i in data['track1'] :
    note = i['note'];
    difference = int(i['end']) - int(i['start']);
    notes.append("new VF.StaveNote({ keys: [\"" + evaluate_note(note) + "\"], duration: \"" + evaluate_difference(difference) + "\" }),");
    current_length = current_length + difference;
    if current_length == stave_length :
        current_length = 0;
        index = index + 1;
        if index % 2 != 0 :
            print("var stave" + str(index) + " = new VF.Stave(" + str(canvas_x) + ", " + str(canvas_y) + ", " + str(canvas_w) + ");");
            print("stave" + str(index) + ".addClef(\"treble\").addTimeSignature(\"4/4\");");
            print("stave" + str(index) + ".setContext(context).draw();");
            print("var notes" + str(index) +  " = [" );
            for i in notes :
                print(i);
            print("];");
            print("Vex.Flow.Formatter.FormatAndDraw(context, stave" + str(index) + ", notes" + str(index) + ");");
            notes = [];
        else :
            print("var stave" + str(index) + " = new VF.Stave(" + str(canvas_x + canvas_w) + ", " + str(canvas_y) + ", " + str(canvas_w) + ");");
            print("stave" + str(index) + ".setContext(context).draw();");
            print("var notes" + str(index) +  " = [" );
            for i in notes :
                print(i);
            print("];");
            print("Vex.Flow.Formatter.FormatAndDraw(context, stave" + str(index) + ", notes" + str(index) + ");");
            notes = [];
            canvas_y = canvas_y + 100;


f.close()


