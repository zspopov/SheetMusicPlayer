var staveCount = 4;
var canvasHeightVar = 220;
var stave1 = new VF.Stave(10, 0, 390);
stave1.addClef("treble").addTimeSignature("4/4");
stave1.setContext(context).draw();
var notes1 = [
new VF.StaveNote({ keys: ["c/4"], duration: "q" }),
new VF.StaveNote({ keys: ["c/4"], duration: "q" }),
new VF.StaveNote({ keys: ["g/4"], duration: "q" }),
new VF.StaveNote({ keys: ["g/4"], duration: "q" }),
];
Vex.Flow.Formatter.FormatAndDraw(context, stave1, notes1);
var stave2 = new VF.Stave(400, 0, 390);
stave2.setContext(context).draw();
var notes2 = [
new VF.StaveNote({ keys: ["a/4"], duration: "q" }),
new VF.StaveNote({ keys: ["a/4"], duration: "q" }),
new VF.StaveNote({ keys: ["g/4"], duration: "h" }),
];
Vex.Flow.Formatter.FormatAndDraw(context, stave2, notes2);
var stave3 = new VF.Stave(10, 100, 390);
stave3.addClef("treble").addTimeSignature("4/4");
stave3.setContext(context).draw();
var notes3 = [
new VF.StaveNote({ keys: ["f/4"], duration: "q" }),
new VF.StaveNote({ keys: ["f/4"], duration: "q" }),
new VF.StaveNote({ keys: ["e/4"], duration: "q" }),
new VF.StaveNote({ keys: ["e/4"], duration: "q" }),
];
Vex.Flow.Formatter.FormatAndDraw(context, stave3, notes3);
var stave4 = new VF.Stave(400, 100, 390);
stave4.setContext(context).draw();
var notes4 = [
new VF.StaveNote({ keys: ["d/4"], duration: "q" }),
new VF.StaveNote({ keys: ["d/4"], duration: "q" }),
new VF.StaveNote({ keys: ["c/4"], duration: "h" }),
];
Vex.Flow.Formatter.FormatAndDraw(context, stave4, notes4);
