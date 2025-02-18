using System;
using System.IO.Ports;
using System.Text;
using System.Threading;

namespace GetDatafromSensors.src.IIoT.sensorComunication
{
    /// <summary>
    /// Handles serial communication with the industrial oven's humidity sensor.
    /// </summary>
    public class SerialCommunicator(string portName, int baudRate, Parity parity, int dataBits, StopBits stopBits)
    {
        private readonly SerialPort _serialPort = new(portName, baudRate, parity, dataBits, stopBits);

        public void OpenConnection()
        {
            _serialPort.Open();

            Console.WriteLine($"Connected to {_serialPort.PortName} port at {_serialPort.BaudRate} baud");
        }

        public string SendCommand(byte[] command)
        {
            Thread.Sleep(1000);
            Console.WriteLine("The command was sent");
            _serialPort.Write(command, 0, command.Length);
            Thread.Sleep(1000);

            Console.WriteLine("Waiting for response...");
            return _serialPort.ReadLine();
        }

        public void CloseConnection()
        {
            if (_serialPort.IsOpen)
            {
                _serialPort.Close();
            }
        }
    }
}
