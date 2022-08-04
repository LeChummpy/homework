args = process.argv.slice(2)
path = args[0]
target_path = args[1]

const fs = require('fs');

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

fs.readFile(path, 'utf8', (err, file_data) => {
  if (err) {
    console.error(err);
    return;
  }
  
let lines = file_data.split("\r\n")
let line_counter = 0

for (let l of lines) {
    line_counter++;
    let cmd_buff = Buffer.alloc(1)
    let av_buff = Buffer.alloc(1)
    
    let line_segments = l.split(" ")
    let command = line_segments[0]
    let args = line_segments.slice(1)
    let n_args = n_required_arg[line_segments[0]]

    let byte_encoding = command_encoding[line_segments[0]]
    let actual_val_addr = null;


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
      
    cmd_buff[0] = byte_encoding;
    av_buff[0] = actual_val_addr;

    } else {
      console.warn("Command in line " + line_counter + "requires " + n_args + " but " + args.length + "args were given.")
    }
    
}

});