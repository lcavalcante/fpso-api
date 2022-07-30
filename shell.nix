{ pkgs ? import <nixpkgs> {} }:
let
  local-python = pkgs.python310;
  python-packages = local-python.withPackages (p: with p; [
    fastapi
    uvicorn
    pynvim
    sqlalchemy
    psycopg2
    alembic
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-packages
    # other dependencies
  ];
  shellHook = ''
    PYTHONPATH=${python-packages}/${python-packages.sitePackages}
    # maybe set more env-vars
  '';
  POSTGRES_HOST="localhost";
  POSTGRES_USER="postgres";
  POSTGRES_PASSWORD="password";
  POSTGRES_DB="db";
}
