//Function takes in a sequence of DNA as a string and returns the amount of each base

var countBases = function(sequence) {
    sequence = sequence.toLowerCase();
    var aCount = 0;
    var tCount = 0;
    var cCount = 0;
    var gCount = 0;
    
    for (i=0; i < sequence.length; i++) {
        if (sequence[i] === 'a') {
            aCount ++;
        }
        else if (sequence[i] === 't') {
            tCount ++;
        }
        else if (sequence[i] === 'c') {
            cCount++;
        }
        else if (sequence[i] === 'g') {
            gCount++;
        }
    }
    
    return 'Adenine = ' + aCount + ' | Thymine = ' + tCount + ' | Cytosine = ' + cCount + ' | Guanine = ' + gCount
}