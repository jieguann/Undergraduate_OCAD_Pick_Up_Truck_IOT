
using System;

using System.Net;

using System.Net.Sockets;

using System.Text;

using System.Threading;

using UnityEngine;





public class TestSocket2 : MonoBehaviour

{



    public string ipAdress;

    public int port;



    private byte[] data = new byte[1024];

    private Socket clientSocket;

    private Thread receiveT;



    void Start()

    {

        ConnectToServer();

    }



    void ConnectToServer()

    {

        try

        {

            clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            clientSocket.Connect(IPAddress.Parse(ipAdress), port);

            Debug.Log("连接服务器成功");

            receiveT = new Thread(ReceiveMsg);

            receiveT.Start();



        }

        catch (System.Exception ex)

        {

            Debug.Log("连接服务器失败！");

            Debug.Log(ex.Message);

        }

    }



    private void ReceiveMsg()

    {

        while (true)

        {

            if (clientSocket.Connected == false)

            {

                Debug.Log("与服务器断开了连接");

                break;

            }



            int lenght = 0;

            lenght = clientSocket.Receive(data);



            string str = Encoding.UTF8.GetString(data, 0, data.Length);

            Debug.Log(str);



        }

    }


    void OnDestroy()

    {

        try

        {

            if (clientSocket != null)

            {

                clientSocket.Shutdown(SocketShutdown.Both);

                clientSocket.Close();//关闭连接

            }



            if (receiveT != null)

            {

                receiveT.Interrupt();

                receiveT.Abort();

            }



        }

        catch (Exception ex)

        {

            Debug.Log(ex.Message);

        }

    }

}
