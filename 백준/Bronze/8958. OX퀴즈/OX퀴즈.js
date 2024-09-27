const fs = require("fs");

let lines = fs.readFileSync(0).toString().trim().split(/\s+/);
lines.shift();

for (str of lines) {
    let [cnt, score] = [0, 0];
    for (i of str){
        if (i == 'O') {
            cnt++;
        }
        else {
            score = score + cnt * (cnt + 1) / 2;
            cnt = 0;
        }
    }
    score = score + cnt * (cnt + 1) / 2;
    console.log(score);
}    
    