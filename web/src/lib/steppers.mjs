export function loopState(step) {
 const states = [
  {line:0,cluster:null,output:[],done:false},
  {line:1,cluster:'COMMS',output:[],done:false},
  {line:2,cluster:'COMMS',output:['COMMS'],done:false},
  {line:1,cluster:'HR',output:['COMMS'],done:false},
  {line:2,cluster:'HR',output:['COMMS','HR'],done:false},
  {line:1,cluster:'HR',output:['COMMS','HR'],done:true}
 ];
 return states[Math.max(0,Math.min(5,step))];
}
export function scoreState(step) {
 const position = Math.max(0,Math.min(5,step));
 const scores = {Events:position>=2?1:0,OSG:position>=4?1:0};
 return {cluster:position===0?null:position<=2?'Events':'OSG', scores, total:scores.Events+scores.OSG, done:position===5,line:position===0?0:position%2?1:2};
}
