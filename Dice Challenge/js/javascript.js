function startGame(){

    var diceOne = random(6,1);
    var diceTwo = random(6,1);

    changeImage('img1',diceOne);
    changeImage('img2',diceTwo);

    if(diceOne > diceTwo){
        document.getElementById('title').innerHTML = "Player 1 Wins🏆";
    }
    else if(diceOne < diceTwo)
    {
        document.getElementById('title').innerHTML = "Player 2 Wins🏆";
    }
    else{
        document.getElementById('title').innerHTML = "Draw!";
    }
}

function random(max,min){
    return Math.floor(Math.random()*6) + 1;
}

function changeImage(img,number){
    switch(number){
        case 1:
            document.getElementById(img).src = 'images/dice1.png';
            break;
        case 2:
            document.getElementById(img).src = 'images/dice2.png';
            break;
        case 3:
            document.getElementById(img).src = 'images/dice3.png';
            break;
        case 4:
            document.getElementById(img).src = 'images/dice4.png';
            break;
        case 5:
            document.getElementById(img).src = 'images/dice5.png';
            break;
        default:
            document.getElementById(img).src = 'images/dice6.png';
    }
}