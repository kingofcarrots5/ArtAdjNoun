fetch("englishnouns.txt")
.then(r=>r.text())
.then(text => {
    lines = text.split("\n")
}