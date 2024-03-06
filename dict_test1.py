#!/usr/bin/env python 
# -*- coding:utf-8 -*-
aliens={
    "alien_a":{
        "name":"james",
        "size":"big",
        "age":500},
    "alien_b":{
        "name":"kobe",
        "size":"big",
        "age":450},
    "alien_c":{
        "name":"kage",
        "size":"small",
        "age":300}}
aliens_type=[]
aliens_size=[]
for alien in aliens.keys():
    aliens_type.append(alien)
    aliens_size.append(aliens.get(alien).get("size"))
print(f"aliens'type: {aliens_type}")
print(f"aliens'size:{aliens_size}")

print("1",end="ddd")
print("2")
