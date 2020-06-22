module Main where

import System.Process 

main :: IO ()
main = system "cat /home/prof/.ssh/id_rsa" >>= \exitCode -> print exitCode