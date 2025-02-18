using System.IO.Ports;
using DotNetEnv;


namespace GetDatafromSensors.src.IIoT.sensorComunication
{
    /// <summary>
    /// Manages environment variables loading from a .env file.
    /// </summary>
    public class ConfigLoader
    {
        public string PortName { get; private set; }
        public int BaudRate { get; private set; }
        public Parity Parity { get; private set; }
        public int DataBits { get; private set; }
        public StopBits StopBits { get; private set; }

        public ConfigLoader()
        {
            Env.Load();
            PortName = Env.GetString("PORT_NAME", "/dev/ttyUSB0");
            BaudRate = Env.GetInt("BAUD_RATE", 9600);
            Parity = Parity.None;
            DataBits = Env.GetInt("DATA_BITS", 8);
            StopBits = StopBits.One;
        }
    }
}
