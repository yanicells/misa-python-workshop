export function loopState(step) {
 const states = [
  {line:0,cluster:null,output:[],done:false},
  {line:1,cluster:'Communications',output:[],done:false},
  {line:2,cluster:'Communications',output:['Communications'],done:false},
  {line:1,cluster:'Human Resources',output:['Communications'],done:false},
  {line:2,cluster:'Human Resources',output:['Communications','Human Resources'],done:false},
  {line:1,cluster:'Human Resources',output:['Communications','Human Resources'],done:true}
 ];
 return states[Math.max(0,Math.min(5,step))];
}
export function scoreState(step) {
 const position = Math.max(0,Math.min(5,step));
 const scores = {Events:position>=2?1:0,'Office of the Secretary General':position>=4?1:0};
 return {cluster:position===0?null:position<=2?'Events':'Office of the Secretary General', scores, total:scores.Events+scores['Office of the Secretary General'], done:position===5,line:position===0?0:position%2?1:2};
}

export function weightedState(step) {
 const position = Math.max(0,Math.min(5,step));
 const scores = {Communications:position>=2?2:0,'Human Resources':position>=4?1:0};
 return {cluster:position===0?null:position<=2?'Communications':'Human Resources', scores, total:scores.Communications+scores['Human Resources'], done:position===5,line:position===0?0:position%2?1:2};
}
