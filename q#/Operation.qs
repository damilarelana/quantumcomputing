namespace HelloWorld {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation SayHello() : Result{
      Message("Hello from the quantum world!");
      return Zero;
    }
}
