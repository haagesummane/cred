## initial thoughts
- need to have each instruction a subclass of 2 axis of 
  - num registers to operate on
    - single register
    - multi register instructions
  - num input params
    - single ip
    - multi ip
    - no ip 
        
- also take care of
    - new register classes
    - new (types of?) instructions
    
additionally, could also go into defining or restricting what registers can/cannot be used with what operations
make a parsed instruction list which can allow/disallow instructions
  - how to handle disallowed instructions? (skip or throw error?)
