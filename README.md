# CSharpPropertyCreator
This is a C# property generator:

It can take any c# file with properties which are in this format:
  > public Type PropertyName { get; set; }
  
And converts it to:
```
        "public type_name public_name { 
                get {
                    return private_name; }
                set {
                    private_name = value; 
                    notifyPropertyChanged(nameof(public_name)); 
            } 
        }
        
        private type_name private_name; " ```
