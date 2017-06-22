@echo off
rd /s /q dota 
rd /s /q steam
mkdir dota 
mkdir steam 
C:\vcpkg\packages\protobuf_x64-windows\tools\protoc.exe --proto_path=../protobufs/dota --cpp_out=dota ../protobufs/dota/*.proto
C:\vcpkg\packages\protobuf_x64-windows\tools\protoc.exe --proto_path=../protobufs/steam --cpp_out=steam ../protobufs/steam/*.proto
echo done.