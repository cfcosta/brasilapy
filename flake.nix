{
  description = "Um cliente da Brasil API em python3";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs = {
        nixpkgs.follows = "nixpkgs";
        flake-utils.follows = "flake-utils";
      };
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; })
          mkPoetryPackages;

        brasilapy = mkPoetryPackages { projectDir = self; };
      in {
        packages = {
          inherit brasilapy;
          default = brasilapy.poetryPackages.brasilapy;
        };

        devShells.default = pkgs.mkShell {
          packages = [ pkgs.poetry ] ++ brasilapy.poetryPackages;
        };
      });
}
