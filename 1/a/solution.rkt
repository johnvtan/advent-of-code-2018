#!/usr/bin/env racket
#lang racket/base
(require racket/file)
(require srfi/1)

(define file-path "input")
(define input (file->lines file-path))

; converts a string (including leading +/- to a numerical value)
(define (to-num str)
  (if (eqv? (string-ref str 0) #\-)
    (* -1 (string->number (substring str 1)))
    (string->number (substring str 1))))

(define (sum L)
  (apply + L))

(display (sum (map to-num input)))
