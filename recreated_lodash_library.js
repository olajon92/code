const _ = {
    clamp(number, lower, upper) {
      let minNum = Math.max(number, lower);
      let clampedNum = Math.min(maxNum, upper);
      return clampedNum; 
      },
    inRange(number, startValue, endValue) {
       if(endValue === undefined){
        endValue = startValue; 
        startValue = 0;
      } if(startValue > endValue){
        let temp = endValue;
        endValue = startValue;
        startValue = temp;
      }if(startValue <= number && number < endValue){
        return true;
      }else {
        return false;
      }
    },
    words(string) {
       const words = string.split(' ');
       return words;
    },
    pad(string, length){
      if (string.length >= length){
        return string
      };
      const startpaddinglength = Math.floor((length - string.length)/2);
      var endpaddingLength = length - string.length - startpaddinglength;
      const paddedstring = ' '.repeat(startpaddinglength) + string + ' '.repeat(endpaddingLength);
      return paddedstring;
    },
    has(object, key){
      const hasvalue = object[key];
      if(hasvalue != undefined){
        return true;
      }
        return false;
      },
  invert(object){
    let invertedobject = {};
    for(let key in object){
      const originalValue = object[key];
      invertedobject = {originalValue: key}
    }
    return invertedobject;
  },
  findKey(object, predicate){
    for(let key in object){
      let value = object[key];
      let predicatereturnvalue = predicate(value);
      if(predicatereturnvalue){
        return key;
      };
    };
    undefined;
    return undefined;
  },
  drop(array, n){
    if(n === undefined){
      n = 1;
    };
    let arraycopy = array.slice(n, array.length);
    return arraycopy;
  },
  dropWhile(array, predicate){
    const callback = (element, index) => {
      return !predicate(element, index, array);
    }
    let dropNumber = array.findIndex(callback);
    let dropArray = this.drop(array, dropNumber);
    return dropArray;
  },
  chunk(array, size=1){
    let arrayChunks = [];
    for (let i=0; i<array.length; i+=size){
      let arrayChunk = array.slice(i, i+size);
      arrayChunks.push(arrayChunk);
    }
    return arrayChunks;
  },
    };






// Do not write or modify code below this line.
module.exports = _;