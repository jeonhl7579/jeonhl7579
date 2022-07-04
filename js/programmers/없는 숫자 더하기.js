function solution(numbers) {
    var answer = 45;
    //i가 요소, j가 인덱스
    let xnum= numbers.map(function(i,j){
        answer-=i
    })
    return answer;
}