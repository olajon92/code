let doorImage1 = document.getElementById('door1');
let doorImage2 = document.getElementById('door2');
let doorImage3 = document.getElementById('door3');
let startButton = document.getElementById('start');
let beachDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/beach.svg'
let spaceDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/space.svg'
let botDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/robot.svg';
var openDoor1,
 openDoor2, 
 openDoor3,
 currentlyPlaying = true;
let closedDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/closed_door.svg';

const isBot = (door) => {
  if(door.src===botDoorPath){
    return true;
  }else{
    return false;
  }
}
 
const isClicked = (door) => {
  if(door.src===closedDoorPath){
    return false;
  }else{
    return true;
  }
} 
const playDoor = (door) => {  
  numClosedDoors--;
  if(numClosedDoors===0){
    gameOver('win');
  }else if(isBot(door)){
    gameOver();
  }
}
doorImage1.onclick = () => { if(!isClicked(doorImage1)&&currentlyPlaying) {doorImage1.src = openDoor1;
playDoor(doorImage1);
}
};
doorImage2.onclick = () => { if(!isClicked(doorImage2)&&currentlyPlaying){doorImage2.src = openDoor2;
playDoor(doorImage2);
}
};
doorImage3.onclick = () => { if(!isClicked(doorImage3)&&currentlyPlaying){doorImage3.src = openDoor3;
playDoor(doorImage3);
}
};
startButton.onclick = () => {
  if(!currentlyPlaying){
    startRound();
}
};
const startRound = () => {
  doorImage1.src = closedDoorPath;
  doorImage2.src = closedDoorPath;
  doorImage3.src = closedDoorPath;
  numClosedDoors = 3;
  startButton.innerHTML = 'Good Luck!'
  currentlyPlaying = true;
  randomChoreDoorGenerator();
}


const gameOver = (status) => {
  if(status==='win'){
    startButton.innerHTML = 'You win! Play Again?';
  }else {
    startButton.innerHTML = 'Game over! Play Again?'
  };
  currentlyPlaying = false;
}

let numClosedDoors = 3;
const randomChoreDoorGenerator = () => {
  let choreDoor = Math.floor(Math.random()*numClosedDoors);
  if(choreDoor===1){
    openDoor1 = botDoorPath;
    openDoor2 = spaceDoorPath;
    openDoor3 = beachDoorPath;
  }else if(choreDoor===2){
    openDoor1 = beachDoorPath;
    openDoor2 = botDoorPath;
    openDoor3 = spaceDoorPath;
  }else{
    openDoor1 = spaceDoorPath;
    openDoor2 = beachDoorPath;
    openDoor3 = botDoorPath;
  }
}
startRound();