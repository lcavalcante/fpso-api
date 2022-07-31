{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.poetry
  ];
  shellHook = ''
    # maybe set more env-vars
  '';
  POSTGRES_HOST="localhost";
  POSTGRES_USER="postgres";
  POSTGRES_PASSWORD="password";
  POSTGRES_DB="db";
}
