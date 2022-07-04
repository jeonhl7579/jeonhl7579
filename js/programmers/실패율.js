function solution(N, stages) {
    var answer =[];
    var peo={};
    let cnt=0;
    var all=stages.length;
    for (let i=0; i<N; i++){
        all=all-cnt;
        cnt=0;
        for (let j=0; j<stages.length; j++){
            if(stages[j]==(i+1)){
                cnt+=1;
            }
        }
        peo[i+1]=cnt/all;
    }
    var sortable=[];
    for (var name in peo){
        sortable.push([Number(name),peo[name]]);
    }
    sortable.sort(function(a,b){
        return b[1]-a[1];
    })
    //console.log(sortable)
    for (let i=0; i<sortable.length; i++){
        answer.push(sortable[i][0]);
    }
    //console.log(peo)
    return answer;
}