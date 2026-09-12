import test from 'node:test';
import assert from 'node:assert/strict';
import {loopState, scoreState, weightedState} from './steppers.mjs';
test('loop separates assignment and print, then stops with last variable retained',()=>{
 assert.deepEqual(loopState(0),{line:0,cluster:null,output:[],done:false});
 assert.deepEqual(loopState(1),{line:1,cluster:'COMMS',output:[],done:false});
 assert.deepEqual(loopState(2),{line:2,cluster:'COMMS',output:['COMMS'],done:false});
 assert.deepEqual(loopState(4),{line:2,cluster:'HR',output:['COMMS','HR'],done:false});
 assert.deepEqual(loopState(5),{line:1,cluster:'HR',output:['COMMS','HR'],done:true});
});
test('weighted awards add two primary points and one related point',()=>{
 assert.deepEqual(weightedState(0),{cluster:null,scores:{COMMS:0,HR:0},total:0,done:false,line:0});
 assert.deepEqual(weightedState(2),{cluster:'COMMS',scores:{COMMS:2,HR:0},total:2,done:false,line:2});
 assert.deepEqual(weightedState(4),{cluster:'HR',scores:{COMMS:2,HR:1},total:3,done:false,line:2});
 assert.equal(weightedState(5).done,true);
 assert.equal(weightedState(0).total,0);
});
test('two awards count as two points and reset clears both',()=>{
 assert.deepEqual(scoreState(0),{cluster:null,scores:{Events:0,OSG:0},total:0,done:false,line:0});
 assert.deepEqual(scoreState(1),{cluster:'Events',scores:{Events:0,OSG:0},total:0,done:false,line:1});
 assert.deepEqual(scoreState(2),{cluster:'Events',scores:{Events:1,OSG:0},total:1,done:false,line:2});
 assert.deepEqual(scoreState(4),{cluster:'OSG',scores:{Events:1,OSG:1},total:2,done:false,line:2});
 assert.equal(scoreState(5).done,true);
 assert.equal(scoreState(0).total,0);
});
