const getUserChoice = userInput => {
 userInput = userInput.toLowerCase();
  if (userInput === 'rock' ||userInput === 'paper' ||userInput === 'scissors'){
    return userInput;
  } else {
    console.log('Error Error');
  }
}
const getComputerChoice = () => {
 let num = Math.floor(Math.random() * 3);
  switch(num){
    case 0:
      return 'rock';
      break;
    case 1:
      return 'paper';
      break;
    case 2:
      return 'scissors';
      break;
  }
}
const Winner = (uchoice, cchoice) => {
  if (uchoice === cchoice){
    return 'Game was a tie!';
  } 
  if (uchoice === 'rock'){
    if (cchoice == 'paper'){
      return 'You lost!!';
    }else {
      return 'You won!!';
    }
  }
  if (uchoice === 'paper'){
    if (cchoice === 'rock'){
      return 'You won!!'
    } else {
      return 'You lost!!';
    }
  }
  if (uchoice === 'scissors'){
    if (cchoice === 'paper'){
      return 'You won!!'
    } else {
      return 'You lost!!';
    }
  }
}
const playgame =  (uchoice, cchoice) => {
 const userchoice = getUserChoice('Rock');
 const cpuchoice = getComputerChoice();
 console.log('You threw ' + userchoice);
 console.log('Computer threw ' + cpuchoice);
 console.log(Winner(userchoice,  cpuchoice));
}
playgame();