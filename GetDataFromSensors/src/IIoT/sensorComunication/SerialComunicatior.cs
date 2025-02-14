using System.IO.Ports;

namespace GetDatafromSensors.src.IIoT.sensorComunication
{
    /// <summary>
    /// Handles serial communication with the industrial oven's humidity sensor.
    /// </summary>
    public class SerialCommunicator(string portName, int baudRate)
    {
        private readonly SerialPort _serialPort = new SerialPort(portName, baudRate, Parity.None, 8, StopBits.One);

        public void OpenConnection()
        {
            _serialPort.Open();
            Console.WriteLine($"Connected to {_serialPort.PortName} at {_serialPort.BaudRate} baud");
        }

        public string SendCommand(string command)
        {
            _serialPort.WriteLine(command);
            Console.WriteLine($"Command sent: {command}");
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
