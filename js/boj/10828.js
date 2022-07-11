let fs=require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num=input.shift();
let arr=[];
let result=[];
for (let i=0; i<num; i++){
    switch(input[i]){
        case 'pop':
            //pop이 안되면 -1출력
            result.push(arr.pop() || -1);
            break;
        case 'size':
            result.push(arr.length);
            break;
        case 'empty':
            result.push(arr[0] ? 0 : 1);
            break;
        case 'top':
            result.push(arr[arr.length-1] || -1);
            break;
        default:
            arr.push(input[i].split(" ")[1]);
            break;
    }
}

console.log(result.join('\n'));