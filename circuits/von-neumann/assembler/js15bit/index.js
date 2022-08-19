function toDez(hex) {
  let encoding = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "a":10,
    "b":11,
    "c":12,
    "d":13,
    "e":14,
    "f":15,
  }

  let reversedhex = hex.split("").reverse()
  let result = 0;
  let potency = 0
  for (let i of reversedhex) {
    val_of_digit = Math.pow(16, potency)
    number_of_digit = encoding[i]
    result += val_of_digit*number_of_digit;
    potency++;
  }
  return result
}

function toBin(dez) {

  result = []
  while (true) {
    let rest = dez%2
    dez = Math.floor(dez/2)
    result.push(rest)

    if (dez==0) {
      return result.reverse().join("")
    }

  }

}

let command_encoding = {
    "ld":0,
    "st":2,
    "add":8,
    "sub":10,
    "cmp":12,
    "psh":14,
    "and":16,
    "or":18,
    "not":20,
    "jlt":22,
    "jgt":24,
    "jeq":26,
    "jmp":28,
    "end":30,
    "out":32,

}

let n_required_arg =  {
  "ld":2,  // v/a + val/addr
  "st":1,  // addr
  "add":2, // v/a + val/addr
  "sub":2, // v/a + val/addr
  "cmp":2, // v/a + val/addr
  "psh":0, //-
  "and":2, // v/a + val/addr
  "or":2,  // v/a + val/addr
  "not":2, // v/a + val/addr
  "jlt":1, //line
  "jgt":1, //line
  "jeq":1, //line
  "jmp":1, //line
  "end":0, //-
  "out":0, //-

}

const fs = require("fs");

let args = process.argv.slice(2)
let path = args[0]
let target_path = args[1]
//let outStream = fs.createWriteStream(target_path)

fs.readFile(path, 'utf8', (err, file_data) => {
  if (err) {
    console.error(err);
    return;
  }

let lines = file_data.split("\r\n")
let line_counter = 0

for (let l of lines) {
    line_counter++;
    //let cmd_buff = Buffer.alloc(1)
    //let av_buff = Buffer.alloc(2)
    let word_buff = Buffer.alloc(3)

    let line_segments = l.split(" ")
    let command = line_segments[0]
    let args = line_segments.slice(1)
    let n_args = n_required_arg[line_segments[0]]

    let byte_encoding = command_encoding[command]
    let actual_val_addr = null;

    if (command in command_encoding) {
      byte_encoding = command_encoding[command]
      actual_val_addr = null;

  } else {
    console.warn("Command in line " + line_counter + " doesn't exist.")
  }


    if (n_args==args.length) {
      if (command=="ld" || command=="add" || command=="sub" || command=="cmp") {
        if (args[0]==1) {
          byte_encoding = byte_encoding + 1;
        }
      } else if (command=="jgt" || command=="jlt" || command=="jeq" || command=="jmp") {
        byte_encoding = byte_encoding + 1;

      }

      if (n_args==2) {
        actual_val_addr = args[1]

      } else if (n_args==1) {
        actual_val_addr = args[0]
      } else {
        actual_val_addr = 0

      }

    //cmd_buff.writeUInt8(byte_encoding, 0);
    //av_buff.writeUInt16BE(actual_val_addr, 0);

    //buff = Buffer.concat([av_buff, cmd_buff])

    word_buff.writeUInt16BE(byte_encoding+actual_val_addr, 0)
    console.log(word_buff)

    //console.log(toBin(3).padStart(6, 0))
    //cmd_bin = toBin(byte_encoding).padStart(6, 0)
    //av_bin = toBin(actual_val_addr).padStart(15, 0)

    //console.log(cmd_bin)

    } else {
      console.warn("Command in line " + line_counter + "requires " + n_args + " but " + args.length + "args were given.")
    }

}

});
