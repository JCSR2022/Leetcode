/**
 * @param {number} numRows
 * @return {number[][]}
 */

var generate = function(numRows) {
    let curr = [1];
    let ans = [[1]];
    
    for (let i = 1; i < numRows; i++) { 
        
        let temp = [0, ...curr, 0];
        let new_curr = [];
        
        for (let j = 0; j < temp.length - 1; j++) {
            new_curr.push(temp[j] + temp[j + 1]);
        }
        
        ans.push(new_curr);
        curr = new_curr;
    }
    
    return ans;
};