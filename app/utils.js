/**
 * Assert an error on failed condition
 * @param {*} condition assertion condition
 * @param {*} message failure message
 */
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

/**
 * Rolls an array. takes the current display index to optimize the search, but may be set to 0 if desired.
 * @param {*} curIndex current display start index
 * @param {*} array array to roll
 * @param {*} roll roll length in seconds
 * @returns display start index
 */
function rollArray(curIndex, array, roll) {
    assert(0 <= curIndex && curIndex < array.length - 1);

    if (roll != 0) {
        let curTime = (new Date()).getTime();
        let rollCutoff = curTime - (roll * 1000);
        rollCutoff = Math.round(rollCutoff);

        for (let i = curIndex; i < array.length; i++) {
            if (array[i][0].getTime() < rollCutoff) {
                curIndex += 1;
            } else {
                break;
            }
        }
    } else {
        curIndex = 0;
    }

    // Clip
    if (curIndex > array.length - 3) {
        curIndex = array.length - 3;
    }

    return curIndex;
}