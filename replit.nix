{ pkgs }: {
  deps = [
    pkgs.python39Full
    pkgs.python39Packages.selenium
    pkgs.chromium
    pkgs.chromedriver
  ];
}