#!/usr/bin/env racket
#lang racket/base
(require racket/file)

(define file-path "input")
(define input (file->lines file-path))

; converts a string (including leading +/- to a numerical value)
(define (to-num str)
  (if (eqv? (string-ref str 0) #\-)
    (* -1 (string->number (substring str 1)))
    (string->number (substring str 1))))

(define (sum L)
  (apply + L))

;(display (sum (map to-num input))) (newline)
(define (pop-last lst)
  (car (reverse lst)))

(define (up-to-last lst)
  (reverse (cdr (reverse lst))))

(define (find-all-sums nums starting-value)
  (define (all-sums-tail-call nums starting-value sum-list)
    (if (null? nums)
      (map (lambda (num) (+ starting-value num)) sum-list)
      (all-sums-tail-call (cdr nums) starting-value (append sum-list (list (+ (car nums) (pop-last sum-list)))))))
  (all-sums-tail-call (reverse nums) starting-value '(0)))
      
(define (find-first-pair lst)
  (cond 
    [(null? lst) #f]
    [else 
      (let ([result (find-first-pair (up-to-last lst))])
        (cond 
          [(number? result) result]
          [(member (pop-last lst) (up-to-last lst)) (pop-last lst)]
          [else #f]))]))
        
(define (find-first-repeating-sum nums starting-value sum-history)
  (let ([all-sums (cdr (find-all-sums nums starting-value))])
    (let ([total-history (append sum-history all-sums)])
      (let ([duplicate (find-first-pair total-history)])
        (if (not duplicate)
          (find-first-repeating-sum nums (pop-last total-history) total-history)
          duplicate)))))

(define nums (reverse (map to-num input)))

;(display (find-all-sums nums 0)) (newline)
(display (find-first-repeating-sum nums 0 '(0))) (newline)

