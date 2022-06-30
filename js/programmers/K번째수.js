function solution(array, commands) {
    var answer = [];
    
    for (let i=0; i<commands.length; i++){
        //console.log(commands[i][0],commands[i][1],commands[i][2])
        var temp=array.slice(commands[i][0]-1,commands[i][1])
        //console.log(temp)
        temp.sort(function(a,b){
            return a-b
        })
        //console.log(temp)
        answer.push(temp[commands[i][2]-1])
    }
    return answer;
}