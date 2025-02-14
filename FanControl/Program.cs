using FanControl.src.IIoT;

/// <summary>
/// Main application entry point.
/// </summary>
class Program
{
    static void Main()
    {
        var config = new ConfigLoader();
        var communicator = new SerialCommunicator(config.PortName, config.BaudRate);

        try
        {
            communicator.OpenConnection();
            int response1 = int.Parse(communicator.SendCommand("STATUS\r\n"));
            Console.WriteLine($"Sensor humidity data: {response1}");
            if (response1 > 30)
            {
                string response2 = communicator.SendCommand("STARFAN\r\n");
                Console.WriteLine($"Fan init status: {response2}");
            }

        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
        finally
        {
            communicator.CloseConnection();
        }
    }
}
